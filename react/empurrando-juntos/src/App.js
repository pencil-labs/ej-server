import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Route,
} from 'react-router-dom';
import Header from './Header';
import Home from './Home';
import Conversations from './Conversations';
import config from './config';
import util from 'util';

import './App.css';

class App extends Component {
  componentDidMount() {
    fetch(`${config.host}/api/v1/users/me/?format=json`, { credentials: 'include' })
      .then(res => res.json())
      .then(
        (result) => {
          window.EJ = window.EJ || {};
          window.EJ.currentUser = result;
          this.forceUpdate();
        },
        (error) => {
          console.log(util.inspect(error));
        }
      )
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Header />
          <div className="App-body">
            <Route exact path="/" component={Home} />
            <Route path="/conversations/:slug" component={Conversations} />
          </div>
        </div>
      </Router>
    );
  }
}

export default App;
