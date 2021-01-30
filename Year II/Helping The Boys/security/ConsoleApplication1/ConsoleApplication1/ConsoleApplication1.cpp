#include <iostream>
#include <set>
#include <cstdint>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
using namespace std;


class AccessPoint
{
private:
    bool mUnlocked;
public:
    AccessPoint()
    {
        mUnlocked = false;
    }
    bool isUnlocked() 
    {
        return mUnlocked;
    }
    void toggle()
    {
        if (mUnlocked)
        {
            mUnlocked = false;
        }
        else
        {
            mUnlocked = true;
        }
    }
};

class AccessDeniedException : public exception
{
}e;

class User
{
protected:
    string mUserId;
    set<uint64_t> mCards;
    vector<AccessPoint*> mAccessPoints;
    uint32_t mActivity;
public:
    User(const string &id)
    {
        this->mUserId = id;
        this->mActivity = 0;
        mCards.clear();
        mAccessPoints.clear();
    }
    void toggleDoor(AccessPoint* ap)
    {
        bool ok = false;
        for (auto i : mAccessPoints)
        {
            if (i == ap)
            {
                i->toggle();
                mActivity++;
                ok = true;
            }
        }
        if (!ok)
        {
            throw AccessDeniedException();
        }
    }
    void addAccessPoint(AccessPoint* ap)
    {
        bool ok = false;
        for (auto i : mAccessPoints)
        {
            if (i == ap)
            {
                ok = true;
            }
        }
        if (!ok)
        {
            mAccessPoints.push_back(ap);
        }
    }
    void addCard(uint64_t x)
    {
        mCards.insert(x);
    }
    bool hasCard(uint64_t x)
    {
        for (auto i : mCards)
        {
            if (i == x)
            {
                return true;
            }
        }
        return false;
    }
    uint32_t countCards()
    {
        return this->mCards.size();
    }
    uint32_t getActivity()
    {
        return this->mActivity;
    }
};

class AdminUser : public User
{
public:
    AdminUser(const string& id):User(id)
    {
    }
    void toggleDoor(AccessPoint* ap)
    {
        ap->toggle();
        this->mActivity++;
    }
};

class Database
{
private:
    map<string, User*> mUsers;
    unordered_map<uint64_t, AccessPoint> mAccessPoints;
public:
    void addUser(const string& s, char c)
    {
        bool ok = false;
        for (auto i : mUsers)
        {
            if (i.first == s)
            {
                ok = true;
            }
        }
        if (!ok)
        {
            if (c == 'U')
            {
                User* u = new User(s);
                mUsers.insert({ s,u });
            }
            else if (c == 'A')
            {
                User* u = new AdminUser(s);
                mUsers.insert({ s,u });
            }
        }
    }
    void addAccessPoint(uint64_t u)
    {
        AccessPoint ap;
        mAccessPoints.insert({ u,ap });
    }
    void addCardToUser(const string& s, uint64_t q)
    {
        mUsers[s]->addCard(q);
    }
    void addAccessPointToUser(const string& s, uint64_t q)
    {
        mUsers[s]->addAccessPoint(&mAccessPoints[q]);
    }
    void parseEvent(uint64_t q, uint64_t x)
    {
        bool ok = false;
        AccessPoint ap;
        for (auto i : mUsers)
        {
            if (i.second->hasCard(q))
            {
                ok = true;
                i.second->toggleDoor(&mAccessPoints[x]);
                break;
            }
        }
        if (!ok)
        {
            throw AccessDeniedException();
        }
    }
    uint32_t countUnlockedDoors()
    {
        uint32_t contor = 0;
        for (auto i : mAccessPoints)
        {
            if (i.second.isUnlocked())
            {
                contor++;
            }
        }
        return contor;
    }
    uint32_t countActivity()
    {
        unsigned contor = 0;
        for (auto i : mUsers)
        {
            contor += i.second->getActivity();
        }
        return contor;
    }
    vector<string> findUsersWithNoCards()
    {
        vector<string> v;
        for (auto i : mUsers)
        {
            if (i.second->countCards() == 0)
            {
                v.push_back(i.first);
            }
        }
        return v;
    }
    uint32_t countCards()
    {
        unsigned contor = 0;
        for (auto i : mUsers)
        {
            contor += i.second->countCards();
        }
        return contor;
    }

};





int main() {
    uint32_t n, m, k;
    std::cin >> n >> m >> k;
    Database database;
    while (n--) {
        uint64_t accessPointId;
        std::cin >> accessPointId;
        database.addAccessPoint(accessPointId);
    }
    while (m--) {
        std::string userId;
        char type;
        std::cin >> userId >> type;
        database.addUser(userId, type);
        uint32_t c;
        std::cin >> c;
        while (c--) {
            uint64_t cardId;
            std::cin >> cardId;
            database.addCardToUser(userId, cardId);
        }
        uint32_t u;
        std::cin >> u;
        while (u--) {
            uint64_t accessPointId;
            std::cin >> accessPointId;
            database.addAccessPointToUser(userId, accessPointId);
        }
    }
    uint32_t errors = 0;

    while (k--) {
        uint64_t accessPointId, cardId;
        std::cin >> accessPointId >> cardId;
        try {
            database.parseEvent(cardId, accessPointId);
        }
        catch (AccessDeniedException& ex) {
            errors++;
        }

    }
    uint32_t subject;
    std::cin >> subject;
    switch (subject) {
    case 1: {
        std::cout << database.countUnlockedDoors();
        break;
    }
    case 2: {
        std::cout << database.countActivity();
        break;
    }
    case 3: {
        auto users = database.findUsersWithNoCards();
        for (const auto& user : users) std::cout << user << " ";
        break;
    }
    case 4: {
        std::cout << database.countCards();
        break;
    }
    case 5: {
        std::cout << errors;
        break;
    }
    }
    return 0;
}
