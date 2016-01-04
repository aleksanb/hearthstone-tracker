var CardList = React.createClass({
	render: function() {
		return (
			<ul className="cards">
				{
					this.props.cards.map(function(card) {
						var inlineCardStyle = {'backgroundImage': `url(https://wow.zamimg.com/images/hearthstone/cards/enus/original/${card.id}.png)`};

						return (
							<li className='card' data-content={card.ids.length > 1 ? '2x' : null}>
								<div className="inline-image" style={inlineCardStyle} />
								<div className="inline-text">{card.name}</div>
							</li>
						);
					})
				}
			</ul>
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
			<div className="players">{
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
