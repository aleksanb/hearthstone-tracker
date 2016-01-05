var CardList = React.createClass({
	render: function() {
		return (
			<ul className="cards">
				{
					this.props.cards.map(function(card) {
						var inlineCardStyle = {'backgroundImage': `url(https://wow.zamimg.com/images/hearthstone/cards/enus/original/${card.id}.png)`};

						return (
							<li className='card'>
								<div className="inline-image" style={inlineCardStyle} />
								<div className="inline-text">{`${card.ids.length}x ${card.name}`}</div>
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
				Object.keys(this.state).sort().map(function(playerId) {
					var player = _this.state[playerId];
					var heroName = player.hero ? player.hero.name : 'Anonymous';
					var playerClass = player.hero ? player.hero.playerClass : 'Anonymous';

					return (
						<div id={'player-' + playerId}>
							<h3>Player {playerId}: {playerClass}</h3>
							<h1>{heroName}</h1>
							<CardList cards={player.cards} />
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
