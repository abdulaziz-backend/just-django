import React from 'react';
import Task from './Task';

interface TaskListProps {
  tasks: any[];
  updateCoins: (newCoins: number) => void;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, updateCoins }) => {
  return (
    <div id="taskContainer" className="task-container">
      {tasks.map(task => (
        <Task key={task.id} task={task} updateCoins={updateCoins} />
      ))}
    </div>
  );
};

export default TaskList;