import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import Uploader from './components/uploader';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="container">
          <header className="m-3">
            <h2>空き家画像判別器</h2>
          </header>
          <Uploader />
        </div>
      </Router>
    );
  }
}

export default App;
