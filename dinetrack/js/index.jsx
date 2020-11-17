import React from 'react';
import PropTypes from 'prop-types';

class Index extends React.Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {};
  }

  componentDidMount() {
  }

  render() {

    return (
      <div>
        <p>
          Hello World of React!
        </p>
      </div>
    );
  }
}

Index.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Index;