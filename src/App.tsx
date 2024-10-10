import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Friends from './components/Friends';
import Navigation from './components/Navigation';
import './App.css';

const App: React.FC = () => {
  return (
    <Router>
      <div className="container">
        <h1 className="retro-title">Just</h1>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/friends" element={<Friends />} />
        </Routes>
        <Navigation />
      </div>
    </Router>
  );
};

export default App;