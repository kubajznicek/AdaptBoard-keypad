import React, { Component } from "react";

import DraggableItem from "./DraggableItem";
import DropTarget from "./DropTarget";

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            nakejtext: "zatim nic",
        };
    }

    componentDidMount() {
        console.log("componentDidMount");
    }

    getText() {
        fetch("https://jsonplaceholder.typicode.com/todos/1")
            .then((result) => result.json())
            .then((result) => {
                this.setState({
                    nakejtext: result.title,
                });
            });
    }

    render() {
        return (
            <div>
                <div>{this.state.nakejtext}</div>
                <button onClick={() => this.getText()}>Get text</button>
                <br />
                <DraggableItem id="item1" image="./images/1.png">Drag me! 1</DraggableItem>
                <DraggableItem id="item2" image="./images/2.png">Drag me! 2</DraggableItem>
                <DraggableItem id="item3">Drag me! pepa</DraggableItem>

                <DropTarget/>
            </div>
        );
    }
}

export default App;
