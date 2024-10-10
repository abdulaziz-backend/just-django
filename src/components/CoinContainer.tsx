import React from 'react';

interface CoinContainerProps {
  coins: number;
}

const CoinContainer: React.FC<CoinContainerProps> = ({ coins }) => {
  return (
    <div className="coin-container">
      <img src="/just.png" alt="Just Icon" className="coin-icon" />
      <div id="coinCounter" className="neon-text">{coins}</div>
    </div>
  );
};

export default CoinContainer;