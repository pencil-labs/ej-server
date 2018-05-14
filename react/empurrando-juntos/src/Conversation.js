import React, { Component } from 'react';
import FontAwesome from 'react-fontawesome';
import { Link } from 'react-router-dom';
import './Conversation.css';

class Conversation extends Component {
  render() {
    const { conversation } = this.props;
    return (
      <div className="Conversation">
        <div className="Conversation-cover">
          <h3>{conversation.title}</h3>
          <p>Assunto: {conversation.category_name}</p>
        </div>
        <div className="Conversation-actions">
          <ul className="Conversation-statistics">
            <li>{conversation.statistics.comments.total} comentários</li>
            <li>{conversation.statistics.votes.total} votos</li>
          </ul>
          <Link to={`/conversations/${conversation.slug}`} className="Conversation-button">Participar <FontAwesome name="comments" style={{ marginLeft: 7 }} /></Link>
        </div>
      </div>
    );
  }
}

export default Conversation;
