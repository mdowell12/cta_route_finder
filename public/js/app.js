// import 'babel-polyfill';

var React = require('react');
var ReactDOM = require('react-dom');
var Masonry = require('react-masonry-component');


var masonryOptions = {
    transitionDuration: 0,
    columnWidth: 1
};

const MASONRY_ITEM_CLASSES = [
    "grid-item-1",
    "grid-item-2",
    "grid-item-3"
]

class Utils {
    static prettyMinutes (s) {
        // console.log(s)
        return Math.round(s);
    };
};

class LeaveTime extends React.Component {

    constructor () {
        super();
    }

    gridItemClass (i) {
        if (i == 0) {
            return 'grid-item-first'
        }

        return MASONRY_ITEM_CLASSES[i % MASONRY_ITEM_CLASSES.length];
    }

    renderLeaveTime (leaveTime) {
        return leaveTime === 0 ? <p>Leave now!</p>
                : <p className="leave-time">Leave in <span className="number">{ leaveTime }</span> mins.</p>
                ;
    }

    render () {
        var routeName = this.props.routeName;
        var leaveTime = Utils.prettyMinutes(this.props.leaveTime);
        var walkTime  = Utils.prettyMinutes(this.props.walkTime);
        var eta       = Utils.prettyMinutes(this.props.eta);
        var color     = this.props.color || "";

        return (
                <div className={`eta-display ${this.gridItemClass(this.props.index)} ${color}`}>
                    <h5>{ routeName }</h5>
                    { this.renderLeaveTime(leaveTime) }
                    <p className="eta-and-walk-time">
                        ({ eta } mins - { walkTime } mins walk time)
                    </p>
                </div>
        );
    }
};

class Container extends React.Component {

    constructor () {
        super();

        this.state = {
            data: null
        };
    }

    componentDidMount () {
        this.getData();
    }

    getData() {
        var self = this;

        fetch('/api')
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            self.setState({data: json});
        })
        .catch(function(response) {console.log(response.message)} )
        ;
    }

    renderLeaveTime(eta, i) {
        return <LeaveTime
                    key={i}
                    index={i}

                    leaveTime={eta.leave_time}
                    walkTime={eta.walk_time_min}
                    eta={eta.eta}
                    routeName={eta.route_name}
                    station={eta.station_name}
                    color={eta.color}
                />
    }

    render () {
        let data = this.state.data;

        if (data) {
            return (
                <div className="container app">
                    <Masonry
                        options={masonryOptions}
                        className="masonry"
                    >
                    {(data.length > 0) ? data.map((eta, i) => this.renderLeaveTime(eta, i)) : "No route found!"}
                    </Masonry>
                </div>
            );
        } else {
            return <h3 className="loading">Loading...</h3>
        }
    }
};

ReactDOM.render(<Container />, document.getElementById('mount-point') );
