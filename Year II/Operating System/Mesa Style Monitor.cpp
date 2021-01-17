#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <unistd.h>
#include <future>
#include <pthread.h>

using namespace std;

mutex singlemtx;

class Monitor
{
private:
#pragma region variables
    volatile int x;
    static Monitor *instance;
    mutex mtx;
    condition_variable noWriters;
    condition_variable noReadWrite;
    bool isWriter;
    unsigned numReaders;
#pragma endregion

#pragma region enter_leave

    void enterRead()
    {
        unique_lock<mutex> lk(mtx);
        while (isWriter)
        {
            noWriters.wait(lk);
        }
        numReaders++;
    }
    void enterWrite(int z)
    {
        unique_lock<mutex> lk(mtx);
        while (!((numReaders == 0) && (!isWriter)))
        {
            cout << 1 << endl;
            noReadWrite.wait(lk);
        }
        x = z;
        isWriter = true;
    }

    int leaveRead()
    {
        unique_lock<mutex> lk(mtx);
        numReaders--;
        if (!numReaders)
            noReadWrite.notify_all();
        return x;
    }

    void leaveWrite()
    {
        unique_lock<mutex> lk(mtx);
        isWriter = false;
        noReadWrite.notify_one();
        noWriters.notify_all();
    }

#pragma endregion

#pragma region ctor
    Monitor()
    {
        x = 0;
        isWriter = false;
        numReaders = 0;
    }
#pragma endregion

public:
#pragma region Singleton
    static Monitor *
    getInstance()
    {
        unique_lock<mutex> lk(singlemtx);
        if (instance)
            return instance;

        else
        {
            return instance = new Monitor;
        }
    }

#pragma endregion

#pragma region func

    void write(int z)
    {
        enterWrite(z);
        leaveWrite();
    }

    int read()
    {
        enterRead();
        return leaveRead();
    }

#pragma endregion
};

Monitor *Monitor::instance = 0;

void writeT(int i)
{
    Monitor::getInstance()->write(i);
}

int readT()
{
    return Monitor::getInstance()->read();
}

int main()
{
    vector<thread> v;
    vector<future<int>> vf;
    for (int i = 0; i < 20; i++)
    {
        v.push_back(thread(writeT, i));
        vf.push_back(async(&readT));
        v.push_back(thread(writeT, i + 10));
    }
    for (int i = 0; i < 20; i++)
    {
        v[i].join();
    }
    for (int i = 0; i < 20; i++)
    {
        cout << vf[i].get() << endl;
    }
    for (int i = 0; i < 20; i++)
    {
        v[20 + i].join();
    }
}