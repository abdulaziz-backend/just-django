import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navigation: React.FC = () => {
  const location = useLocation();

  return (
    <nav>
      <Link to="/" className={`nav-button ${location.pathname === '/' ? 'active' : ''}`} aria-label="Home">
        <i className="fas fa-home"></i>
      </Link>
      <Link to="/friends" className={`nav-button ${location.pathname === '/friends' ? 'active' : ''}`} aria-label="Frens">
        <i className="fas fa-users"></i>
      </Link>
    </nav>
  );
};

export default Navigation;