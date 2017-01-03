var LeaveTime = React.createClass({
    render: function() {
        console.log(this.props.leaveTime);
        let data = this.props.leaveTime;

        if (data.leave_time < 0) {
            return null;
        } else {
            return (
                <div className="eta-display">
                    <div>
                        <h3>{data.station_name}</h3>
                    </div>

                    <div>
                        <h5>{ data.route_name }</h5>
                        <span className="leave-time">
                            Leave in { data.leave_time } mins.
                        </span>
                        <span className="eta-and-walk-time">
                            ({ data.eta } mins - { this.props.walkTime } mins walk time)
                        </span>
                    </div>
                </div>
            );
        }
    }
});

var Container = React.createClass({
    getInitialState() {
        return {data: null};
    },

    getData(self) {
        fetch('/api')
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            self.setState({data: json});
        })
        .catch(function(response) {console.log(response.message)} )
        ;
    },

    renderETA(item) {
        return item.leave_times.map(function(lt) {
            return <LeaveTime leaveTime={lt} walkTime={item.walk_time_min} />;
        })
    },

    componentDidMount() {
        this.getData(this);
    },

    render: function() {
        console.log(this.state);
        return (
            <div className="container">
                {this.state.data ? this.state.data.map(this.renderETA) : null}
            </div>
        );
    }
});
React.render(<Container />, document.getElementById('mount-point') );
