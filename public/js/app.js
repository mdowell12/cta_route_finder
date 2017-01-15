// import 'babel-polyfill';

var React = require('react');
var ReactDOM = require('react-dom');
var Masonry = require('react-masonry-component');

var masonryOptions = {
    transitionDuration: 0
};

class Utils {
    static prettyMinutes (s) {
        return Math.round(s);
    };
};

class LeaveTime extends React.Component {

    constructor () {
        super();
    }

    renderLeaveTime (leaveTime) {
        return leaveTime === 0 ? <p>Leave now!</p>
                : <p className="leave-time">Leave in <span className="number">{ leaveTime }</span> mins.</p>
                ;
    }

    render () {
        // console.log(this.props.leaveTime);
        let data = this.props.leaveTime;

        let routeName = data.route_name;
        let leaveTime = Utils.prettyMinutes(data.leave_time);
        let walkTime  = Utils.prettyMinutes(this.props.walkTime);
        let eta       = Utils.prettyMinutes(data.eta);

        if (data.leave_time < 0) {
            return null;
        } else {
            return (
                <Masonry
                    options={masonryOptions}
                >
                    <div className="eta-display">
                        <h5>{ routeName }</h5>
                        { this.renderLeaveTime(leaveTime) }
                        <p className="eta-and-walk-time">
                            ({ eta } mins - { walkTime } mins walk time)
                        </p>
                    </div>
                </Masonry>
            );
        }
    }
};

class Container extends React.Component {

    constructor () {
        super();
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
        return item.leave_times.map((lt, j) => <LeaveTime key={j} leaveTime={lt} walkTime={item.walk_time_min} />)
    }

    render () {
        if (this.state) {
            let data = this.state.data;

            return (
                <div className="container">
                    {data ? data.map(obj => this.renderETA(obj)) : "No route found!"}
                </div>
            );
        } else {
            return <h3>Loading...</h3>
        }
    }
};

ReactDOM.render(<Container />, document.getElementById('mount-point') );
