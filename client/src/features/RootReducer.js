import BusSlice from "./BusSlice";
import AuthSlice from "./AuthSlice";
import { UserAuthApi } from "../auth/UserAuthApi";
import { combineReducers } from "redux";

const rootReducer = combineReducers({
    BusSlice,
    [UserAuthApi.reducerPath]: UserAuthApi.reducer,
    AuthSlice
})

export default rootReducer;