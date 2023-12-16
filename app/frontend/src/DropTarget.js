import React, { Component } from "react";

import "./styles/DropTarget.css";
import DraggableItem from "./DraggableItem";

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
                {/* {this.state.droppedItem && <div>{this.state.droppedItem.content}</div>} */}
                {this.state.droppedItem && <DraggableItem image={this.state.droppedItem.image}>{this.state.droppedItem.content}</DraggableItem>}

            </div>
        );
    }
}

export default DropTarget;
