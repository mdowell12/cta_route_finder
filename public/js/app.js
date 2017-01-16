// import 'babel-polyfill';

var React = require('react');
var ReactDOM = require('react-dom');
var Masonry = require('react-masonry-component');


var masonryOptions = {
    transitionDuration: 0
};

const MASONRY_ITEM_CLASSES = [
    "grid-item-1",
    "grid-item-2",
    "grid-item-3"
]

class Utils {
    static prettyMinutes (s) {
        return Math.round(s);
    };
};

class LeaveTime extends React.Component {

    constructor () {
        super();
    }

    gridItemClass (i) {
        return MASONRY_ITEM_CLASSES[i % MASONRY_ITEM_CLASSES.length];
    }

    renderLeaveTime (leaveTime) {
        return leaveTime === 0 ? <p>Leave now!</p>
                : <p className="leave-time">Leave in <span className="number">{ leaveTime }</span> mins.</p>
                ;
    }

    render () {
        let data = this.props.leaveTime;

        let routeName = data.route_name;
        let leaveTime = Utils.prettyMinutes(data.leave_time);
        let walkTime  = Utils.prettyMinutes(this.props.walkTime);
        let eta       = Utils.prettyMinutes(data.eta);
        let color     = data.color || "";

        if (data.leave_time < 0) {
            return null;
        } else {
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

    renderETA(item) {
        return item.leave_times.map((lt, j) => <LeaveTime key={j} index={j} leaveTime={lt} walkTime={item.walk_time_min} />)
    }

    render () {
        if (this.state.data) {
            let data = this.state.data;

            return (
                <div className="container app">
                    <Masonry
                        options={masonryOptions}
                        className="masonry"
                    >
                    {data ? data.map(obj => this.renderETA(obj)) : "No route found!"}
                    </Masonry>
                </div>
            );
        } else {
            return <h3 className="loading">Loading...</h3>
        }
    }
};

ReactDOM.render(<Container />, document.getElementById('mount-point') );
