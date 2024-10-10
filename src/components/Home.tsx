import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CoinContainer from './CoinContainer';
import TaskList from './TaskList';

const Home: React.FC = () => {
  const [coins, setCoins] = useState(0);
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchUserData();
    fetchTasks();
  }, []);

  const fetchUserData = async () => {
    try {
      const response = await axios.get('/api/user/');
      setCoins(response.data.coins);
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  const fetchTasks = async () => {
    try {
      const response = await axios.get('/api/tasks/');
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  const updateCoins = (newCoins: number) => {
    setCoins(newCoins);
  };

  return (
    <div id="home" className="page active">
      <CoinContainer coins={coins} />
      <h2 className="retro-title">Tasks</h2>
      <TaskList tasks={tasks} updateCoins={updateCoins} />
    </div>
  );
};

export default Home;