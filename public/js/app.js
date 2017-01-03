var LeaveTime = React.createClass({
    render: function() {
        console.log(this.props.item);
        let data = this.props.item;

        return (
            <div className="eta-display">
                <h3>{data.station_name}</h3>
            </div>
        );
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

    renderLeaveTime(item) {
        return <LeaveTime item={item} />;
    },

    componentDidMount() {
        this.getData(this);
    },

    render: function() {
        console.log(this.state);
        return (
            <div>
                {this.state.data ? this.state.data.map(this.renderLeaveTime) : null}
            </div>
        );
    }
});
React.render(<Container />, document.getElementById('mount-point') );

/*
{% if stop.has_nonnegative_leave_time %}
    {% for lt in stop.leave_times %}

            {% if lt.leave_time > 0 %}
                <div class="eta-display">
                <h3>{{ stop.station_name}}</h3>
                <h5>{{ lt.route_name | route_name_map }}</h5>
                <span class="leave-time">
                    Leave in {{ lt.leave_time | pretty_minutes }}
                </span>
                <span class="eta-and-walk-time">
                    ({{ lt.eta | pretty_minutes }} - {{ lt.walk_time_min | pretty_minutes}} walk time)
                </span>
                </div>
            {% endif %}

    {% endfor %}
    {% else %}
    <div class="eta-display">
        {{ stop.station_name}}
        <p>You better run because next one comes in {{ stop.leave_times[0].eta | pretty_minutes }}.</p>
    </div>
    {% endif %}

*/