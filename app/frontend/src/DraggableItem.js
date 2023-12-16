import React, { Component } from "react";

import "./styles/DraggableItem.css";

class DraggableItem extends React.Component {
    handleDragStart = (event) => {
        event.dataTransfer.setData("text/plain", JSON.stringify({ id: this.props.id, content: this.props.children }));
    };

    render() {
        return (
            <div className="draggable-item" draggable onDragStart={this.handleDragStart}>
                {this.props.children}
            </div>
        );
    }
}

export default DraggableItem;
