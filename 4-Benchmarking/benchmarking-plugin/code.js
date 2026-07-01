/**
 * Benchmarking viewport snap plugin
 * Snaps Figma viewport to named frames in sequence for controlled user testing
 * Reference: Claude Sonnet 4.6
 */
const tasks = [
  "Please zoom in 5 times so that after each zoom the coloured box outline aligns with the viewport outline, please briefly pause before each zoom.",
  "Please pan to the right 5 times to centre the coloured box on screen after each pan, please briefly pause before each pan.",
  "Please use a combination of panning and zooming to focus in on one coloured box at a time. After focusing on one box press re-snap to reset the canvas and then focus in on the next box.",
  "Please click on each box one at a time.",
  "Please click on each box one at a time.",
  "Please click on each box one at a time.",
  "Please multiselect one set of coloured boxes at a time (e.g. make sure all boxes of the same colour are selected - and then repeat for each colour).",
  "Please multiselect one set of coloured boxes at a time (e.g. make sure all boxes of the same colour are selected - and then repeat for each colour).",
  "Please type the text in the specified locations.",
  "Please create 5 rectangles to the right of the existing rectangle. They can be any shape or size.",
  "Please create 5 rectangles in the specified positions.",
  "Please create 5 rectangles in the specified positions.",
  "Please move the 5 dark blue five rectangles to the right into the gaps in the light blue pattern on the left, making sure they are aligned correctly.",
  "Please drag the 5 rectangles to increase the sizes to the desired positions.",
];

var index = 0;
var frames = [];
var count = (function () {
  var all = figma.currentPage.findAll(function (n) {
    return n.type === "FRAME" && /^benchmark-\d+$/.test(n.name);
  });
  all.sort(function (a, b) {
    return parseInt(a.name.split("-")[1]) - parseInt(b.name.split("-")[1]);
  });
  frames = all;
  return all.length;
})();

figma.showUI(__html__, { width: 480, height: 90, title: "Tasks" });
snapTo(0);

figma.ui.onmessage = function (msg) {
  if (msg === "next" && index < count - 1) snapTo(++index);
  if (msg === "prev" && index > 0) snapTo(--index);
  if (msg === "snap") {
    var center = figma.viewport.center;
    var nearest = 0;
    var nearestDist = Infinity;
    frames.forEach(function (f, j) {
      var dx = (f.x + f.width / 2) - center.x;
      var dy = (f.y + f.height / 2) - center.y;
      var dist = dx * dx + dy * dy;
      if (dist < nearestDist) { nearestDist = dist; nearest = j; }
    });
    snapTo(index = nearest);
  }
  if (msg.type === "goto") {
    var i = parseInt(msg.value) - 1;
    if (i >= 0 && i < count) snapTo(index = i);
  }
};

function snapTo(i) {
  var target = frames[i];
  if (!target) { figma.ui.postMessage({ status: "Frame not found: benchmark-" + (i + 1), instruction: "" }); return; }
  var vb = figma.viewport.bounds;
  var zoom = Math.min((vb.width * figma.viewport.zoom) / target.width, (vb.height * figma.viewport.zoom) / target.height);
  figma.viewport.zoom = zoom;
  figma.viewport.center = { x: target.x + target.width / 2, y: target.y + target.height / 2 };
  figma.ui.postMessage({ status: (i + 1) + " / " + count, instruction: tasks[i] || "" });
}