// figma.showUI(__html__, { width: 400, height: 200 });
figma.showUI(__html__, { width: 0, height: 0 });

// messages have this structure:
// {{"type": "select", "query": "Layer Name"}}

figma.ui.onmessage = async (msg) => {
    await handleCommand(msg);
};

async function handleCommand(msg) {
    console.log(msg);
    if (msg.type === "select") {

        const objects = msg.query;

        const nodes = objects
            .map(q => figma.currentPage.findOne(n => n.name === q))
            .filter(Boolean)

        figma.currentPage.selection = nodes
    }

    // zoom onto single object
    if (msg.type === "object zoom") {
        const node = figma.currentPage.findOne(n => n.name === msg.query)

        if (node) {
            figma.viewport.scrollAndZoomIntoView([node]);
        }
    }

    // zoom
    if (msg.type === "zoom") {
        figma.viewport.zoom = msg.query;
    }

    // pan
    if (msg.type === "pan") {
        const coords = msg.query;
        const x_pan = coords["x"];
        const y_pan = coords["y"];

        //  get current viewport centre
        const center = figma.viewport.center;

        figma.viewport.center = {
            x: center.x + x_pan,
            y: center.y + y_pan
        };

    }

    // centre object
    if (msg.type === "object pan") {
        const node = figma.currentPage.findOne(n => n.name === msg.query)

        if (node && node.absoluteBoundingBox) {
            // Scroll so node is centered
            figma.viewport.center = {
                x: node.absoluteBoundingBox.x + node.absoluteBoundingBox.width / 2,
                y: node.absoluteBoundingBox.y + node.absoluteBoundingBox.height / 2
            };
        };
    }

    // move object
    if (msg.type === "move") {
        const node = figma.currentPage.findOne(n => n.name === msg.query);
        if (node) {
            node.x = msg.x;
            node.y = msg.y;
        }
    }

    // resize
    if (msg.type === "resize") {
        const node = figma.currentPage.findOne(n => n.name === msg.query);
        if (node) {
            const newWidth = node.width * (msg.factor);
            const newHeight = node.height * (msg.factor);
            node.resize(newWidth, newHeight);
        }
    }

    // create rectangle
    if (msg.type === "create rect") {
        const rect = figma.createRectangle();
        rect.x = msg.x;
        rect.y = msg.y;
        rect.resize(msg.width || 100, msg.height || 100);
        figma.currentPage.appendChild(rect);
    }

    // create text
    if (msg.type === "create text") {
        await figma.loadFontAsync({ family: "Inter", style: "Regular" });
        const text = figma.createText();
        text.x = msg.x;
        text.y = msg.y;
        text.characters = msg.content || "Text";
        figma.currentPage.appendChild(text);
    }

    if (msg.type === "zoom fit") {
        const nodes = figma.currentPage.findAll();
        if (nodes.length > 0) {
            figma.viewport.scrollAndZoomIntoView(nodes);
        }
    }
}

async function pollCommand() {
    try {
        const res = await fetch("http://localhost:8000/command");
        const data = await res.json();

        if (data.command) {
            await handleCommand(data.command);
        }
    } catch (e) {
        console.error(e);
    }
}

setInterval(pollCommand, 2000);

async function sendData() {
    // find all the nodes on the current page
    const nodes = figma.currentPage.findAll(n => n.visible);

    const payload = {
        nodes: nodes.map(n => {
            const bbox = n.absoluteBoundingBox || {
                x: 0, y: 0, width: 0,
                height: 0
            };
            return {
                id: n.id,
                name: n.name,
                type: n.type,
                x: bbox.x,
                y: bbox.y,
                width: bbox.width,
                height: bbox.height
            };
        }),
        viewport: {
            x: figma.viewport.bounds.x,
            y: figma.viewport.bounds.y,
            zoom: figma.viewport.zoom
        },
        currently_selected_object: figma.currentPage.selection
    };

    try {
        await fetch("http://localhost:8000/update", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    } catch (e) {
    }
}

sendData();

figma.on("selectionchange", sendData);
figma.on("currentpagechange", sendData);