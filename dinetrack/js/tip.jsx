import React from 'react';
import PropTypes from 'prop-types';

class Tip extends React.Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
        inputAmount: '',
        tipPercentage: '',
        tipToPay: '',
    };
  }

  componentDidMount() {
  }

  handleClick(event) {
    const value = event.target.value; 
    switch(value) {
        case 'submit': {
            var currTipToPay = '';
            if (this.inputAmount !== '' && this.tipPercentage !== '') {
                currTipToPay = calculateTip(this.inputAmount, this.tipPercentage);
                if (currTipToPay===undefined) 
                    this.setState({tipToPay: "Math Error"}); 
                else
                    this.setState({ tipToPay: currTipToPay}); 
                break; 
            }
        }
    }
  }
  
  calculateTip(_inputAmount, _tipPercentage) {
    return _inputAmount * _tipPercentage / 100;
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

Tip.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Tip;