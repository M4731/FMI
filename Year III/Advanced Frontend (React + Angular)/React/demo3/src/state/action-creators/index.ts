import {ActionType} from '../action-types/index'
import {Dispatch} from 'redux'
import {Action} from '../actions/index'


export const depositMoney = (amount:number) => {
    return (dispatch : Dispatch<Action>) => 
        dispatch({
            type : ActionType.DEPOSIT,
            payload : amount
    })
}

export const withdrawMoney = (amount:number) => {
    return (dispatch : Dispatch<Action>) => 
        dispatch({
            type : ActionType.WITHDRAW,
            payload : amount
    })
}

export const bankrupt = () => {
    return (dispatch : Dispatch<Action>) => 
        dispatch({ 
            type : ActionType.BANKRUPT,
    })
}