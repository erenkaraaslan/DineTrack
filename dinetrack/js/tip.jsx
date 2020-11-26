import React from 'react';
import PropTypes from 'prop-types';

class Tip extends React.Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
        name: '',
        slideValue: '',
        inputAmount: '',
        tipPercentage: '',
        tipToPay: '',
    };

    this.updateName = this.updateName.bind(this);
    this.updateAmount = this.updateAmount.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.setState({
      tipPercentage: '20',
      slideValue: '20',
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

  handleClick(event) {
    event.preventDefault();
    console.log("Here");
    console.log(this.state.slideValue);
    this.setState({
      tipPercentage: this.state.slideValue,
      tipToPay: (this.state.inputAmount * this.state.slideValue / 100.0).toFixed(2),
    });
    console.log(this.state.tipToPay);
  }

  handleChange(event) {
    event.preventDefault();
    this.setState({
      slideValue: event.target.value,
    });
  }

  render() {
    let output;
    if(this.state.tipToPay) {
      output = <p>{this.state.name} must tip ${this.state.tipToPay} at {this.state.tipPercentage} percent tip.</p>;
    }
    return (
      <div className="tip">
        <input type="text" placeholder="Name" value={this.state.name} onChange={this.updateName}/>
        <input type="text" placeholder="Amount" value={this.state.inputAmount} onChange={this.updateAmount}/>
        <p>{this.state.slideValue}%</p>
        <input type="range" min="0" max="100" step="1" value={this.state.slideValue} onChange={this.handleChange}/>
        <button onClick={this.handleClick}>Calculate Tip!</button>
        {output}
      </div>
    );
  }
}

class TipIndex extends React.Component {
  constructor(props) {
    super(props);
    this.state = {numTippers: '', tipList: []};
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleParty = this.handleParty.bind(this);
  }

  componentDidMount() {
    this.setState({
      numTippers: '',
    });
  }

  handleParty(event) {
    event.preventDefault();
    this.setState({
      numTippers: event.target.value,
    });
  }

  handleSubmit(event) {
    console.log("Here");
    event.preventDefault();
    let tips = [];
    for(let i = 0; i < this.state.numTippers; ++i) {
      let iString = i.toString();
      let tip = {
        id: iString
      };
      let jsonTip = JSON.stringify(tip);
      console.log(jsonTip);
      tips.push(jsonTip);
    }
    this.setState({
      numTippers: '',
      tipList: tips,
    });
  }

  render() {
    const tipItems = this.state.tipList.map((tip, index) => (
      <div key={index}>
        <Tip/>
        <br/>
      </div>
    ));
    return (
      <div>
        <p>How many people will be paying for this meal?</p>
        <form onSubmit={this.handleSubmit}>
          <input type="text" placeholder="Party Size" value={this.state.numTippers} onChange={this.handleParty}/>
        </form>
        <br/>
        {tipItems}
      </div>
    );
  }
}

export default TipIndex;