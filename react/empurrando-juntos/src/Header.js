import React, { Component } from 'react';
import logo from './logo.svg';
import './Header.css';

class Header extends Component {
  render() {
    let user = null;
    if (window.EJ) {
      user = window.EJ.currentUser;
    }

    return (
      <div className="Header">
        <img src={logo} className="Header-logo" alt="logo" />
        { user ? <span>Olá, {user.name || user.username}!</span> : null }
        <br style={{ clear: 'both' }} />
      </div>
    );
  }
}

export default Header;
