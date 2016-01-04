var CardList = React.createClass({
	render: function() {
		return (
			<div className="cards">
				{
					this.props.cards.map(function(card) {
						var cardText = `${card.cost} - ${card.ids.length}x ${card.name} (${card.id})`
						return <div>{cardText}</div>
					})
				}
			</div>
		);
	}
});

var Players = React.createClass({
	loadPlayersState: function() {
		var _this = this;
		let req = new XMLHttpRequest();
		req.addEventListener('load', function() {
			var players = JSON.parse(this.responseText)
			_this.setState(players);
		});
		req.open('GET', this.props.url);
		req.send();
	},

	getInitialState: function() {
		return {};
	},

	componentDidMount: function() {
		this.loadPlayersState();
		setInterval(this.loadPlayersState, this.props.pollInterval);
	},

	render: function() {
		console.log(this.state)
		var _this = this;
		return (
			<div>{
				Object.keys(this.state).map(function(player) {
					return (
						<div id={'player-' + player}>
							<h1>Player {player}</h1>
							<CardList cards={_this.state[player]} />
						</div>
					)
				})
			}</div>
		);
	}

});

ReactDOM.render(
	<Players url="http://localhost:8888" pollInterval={1000}/>,
	document.getElementById('players')
);
