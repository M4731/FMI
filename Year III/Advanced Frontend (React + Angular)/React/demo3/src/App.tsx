import React, {useState} from 'react';
import './App.css';
import {actionCreators, State} from './state';
import {useDispatch, useSelector} from 'react-redux';
import {bindActionCreators} from 'redux';

function App() {
  const dispatch = useDispatch();
  const {depositMoney, withdrawMoney, bankrupt} = bindActionCreators(
    actionCreators, 
    dispatch
  );

  const amount = useSelector ((state : State) => state.bank);

  const[depositValue, setDepositValue] = useState(0);

  return (
    <div className="App">
      <h1>{amount}</h1>

      <input 
        type="number" 
        value={depositValue} 
        onChange={(e) => {
        if(e.target.value === '') {
          setDepositValue(0);
        } else {
          setDepositValue(parseInt(e.target.value))
        }
      }}
      />

      <button onClick={() => depositMoney(depositValue)}>deposit</button>
      <button onClick={() => withdrawMoney(depositValue)}>withdraw</button>
      <button onClick={() => bankrupt()}>bankrupt</button>
    </div>
  );
}

export default App;
