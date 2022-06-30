import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import {
    BrowserRouter as Router,
    Route,
    Routes,
    Link,
    Redirect,
} from 'react-router-dom';
export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path="/">
                        <p>This is the home</p>
                    </Route>
                    <Route exact path="/join" element={<RoomJoinPage />} />
                    <Route exact path="/create" element={<CreateRoomPage />} />
                </Routes>
            </Router>
        );

    }

}
