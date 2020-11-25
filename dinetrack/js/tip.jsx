import React from 'react';
import PropTypes from 'prop-types';

let uniqueIndex = 0;

function updateState(percent) {
  this.setState({
      tipPercentage: percent,
      tipToPay: this.state.inputAmount * percent / 100.0,
  });
}

function addUnique(index) {
  this.setState({
      id: index,
  });
  uniqueIndex++;
}

class Tip extends React.Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
        id: '',
        name: '',
        inputAmount: '',
        tipPercentage: '',
        tipToPay: '',
    };
    updateState = updateState.bind(this);
    this.updateName = this.updateName.bind(this);
    this.updateAmount = this.updateAmount.bind(this);
    //this.handleTip = this.handleTip.bind(this);
  }

  componentDidMount() {
    this.setState({
      tipPercentage: '20',
    });
  }

  updateName(event) {
    this.setState({
      name: event.target.value,
    });
  }

  updateAmount(event) {
    this.setState({
      inputAmount: event.target.value,
    });
  }

  /*handleTip(event) {
    event.preventDefault();
    console.log("In handleTip");
    this.setState({
      tipToPay: this.state.inputAmount * this.state.tipPercentage / 100.0,
    });
  }*/

  render() {
    let output;
    if(this.state.tipToPay) {
      output = <p>{this.state.name} must tip {this.state.tipToPay} at {this.state.tipPercentage} percent</p>;
    }
    return (
      <div className="tip">
        <input type="text" placeholder="Name" value={this.state.name} onChange={this.updateName}/>
        <input type="text" placeholder="Amount" value={this.state.inputAmount} onChange={this.updateAmount}/>
        {output}
      </div>
    );
  }
}

class TipIndex extends React.Component {
  constructor(props) {
    super(props);
    this.state = {numTippers: '', slideValue: '', tipList: []};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleParty = this.handleParty.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    this.setState({
      slideValue: 20,
      numTippers: 0,
    });
  }

  handleParty(event) {
    event.preventDefault();
    this.setState({
      numTippers: event.target.value,
    });
  }

  handleChange(event) {
    event.preventDefault();
    this.setState({
      slideValue: event.target.value,
    });
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state.numTippers);
  }

  handleClick(event) {
    event.preventDefault();
    updateState(this.state.slideValue);
  }

  render() {
    const tip = <Tip/>;
    return (
      <div>
        <p>How many people will be paying for this meal?</p>
        <form onSubmit={this.handleSubmit}>
          <input type="text" placeholder="Party Size" value={this.state.numTippers} onChange={this.handleParty}/>
        </form>
        {tip}
        <div>
          <p>{this.state.slideValue}%</p>
          <input type="range" min="0" max="100" step="1" value={this.state.slideValue} onChange={this.handleChange}/>
          <button onClick={this.handleClick}>Calculate Tip!</button>
        </div>
      </div>
    );
  }
}

export default TipIndex;