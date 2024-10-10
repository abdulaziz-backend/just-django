import React, { useState } from 'react';
import axios from 'axios';

interface TaskProps {
  task: any;
  updateCoins: (newCoins: number) => void;
}

const Task: React.FC<TaskProps> = ({ task, updateCoins }) => {
  const [status, setStatus] = useState(task.status);
  const [cooldown, setCooldown] = useState(task.cooldown);

  const startTask = async () => {
    try {
      const response = await axios.post(`/api/tasks/${task.id}/start/`);
      setStatus('claiming');
      setTimeout(() => {
        setStatus('claim');
      }, 5000);
    } catch (error) {
      console.error('Error starting task:', error);
    }
  };

  const claimTask = async () => {
    try {
      const response = await axios.post(`/api/tasks/${task.id}/claim/`);
      updateCoins(response.data.coins);
      setStatus('start');
      setCooldown(60);
      startCooldown();
    } catch (error) {
      console.error('Error claiming task:', error);
    }
  };

  const startCooldown = () => {
    const interval = setInterval(() => {
      setCooldown(prevCooldown => {
        if (prevCooldown === 1) {
          clearInterval(interval);
          return 0;
        }
        return prevCooldown - 1;
      });
    }, 1000);
  };

  return (
    <div className="task">
      <div className="task-info">
        <i className={`fas ${task.icon} task-icon`}></i>
        <div>
          <div className="task-name">{task.name}</div>
          <div className="task-prize">Prize: {task.prize} coins</div>
        </div>
      </div>
      <button
        className="pixel-button task-button"
        onClick={status === 'claim' ? claimTask : startTask}
        disabled={status === 'claiming' || cooldown > 0}
      >
        {cooldown > 0 ? `${cooldown}s` : status === 'claiming' ? <div className="spinner"></div> : status === 'claim' ? 'Claim' : 'Start'}
      </button>
    </div>
  );
};

export default Task;