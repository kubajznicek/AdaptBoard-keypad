import React, { Component } from "react";

import "./styles/DropTarget.css";

class DropTarget extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            droppedId: null,
            droppedItem: null,
        };
    }

    handleDragOver = (event) => {
        event.preventDefault();
    };

    handleDrop = (event) => {
        event.preventDefault();
        const droppedItem = JSON.parse(event.dataTransfer.getData("text/plain"));
        this.setState({ droppedItem });
    };

    render() {
        return (
            <div className="drop-area" onDragOver={this.handleDragOver} onDrop={this.handleDrop}>
                {this.state.droppedItem && <div>{this.state.droppedItem.content}</div>}
            </div>
        );
    }
}

export default DropTarget;
