import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Friends: React.FC = () => {
  const [friends, setFriends] = useState(0);
  const [referralLink, setReferralLink] = useState('');

  useEffect(() => {
    fetchFriendsData();
  }, []);

  const fetchFriendsData = async () => {
    try {
      const response = await axios.get('/api/user/friends/');
      setFriends(response.data.friends_count);
      setReferralLink(response.data.referral_link);
    } catch (error) {
      console.error('Error fetching friends data:', error);
    }
  };

  const inviteFriend = async () => {
    try {
      await axios.post('/api/user/invite/');
      // The backend will handle updating the user's coin count
      fetchFriendsData();
    } catch (error) {
      console.error('Error inviting friend:', error);
    }
  };

  return (
    <div id="friends" className="page">
      <h2 className="retro-title">Frens</h2>
      <div className="friends-container">
        <div id="friendCounter" className="friend-counter">{friends}</div>
        <p>Frens Invited</p>
      </div>
      <div className="invite-container">
        <h3>Invite more frens</h3>
        <p>100 coins per fren</p>
        <p>MORE frens = MORE coins</p>
        <button id="inviteFriendsButton" className="pixel-button" onClick={inviteFriend}>
          <i className="fas fa-user-plus"></i> Invite Frens
        </button>
        {referralLink && (
          <div className="referral-link">
            <p>Your referral link:</p>
            <input type="text" value={referralLink} readOnly />
          </div>
        )}
      </div>
    </div>
  );
};

export default Friends;