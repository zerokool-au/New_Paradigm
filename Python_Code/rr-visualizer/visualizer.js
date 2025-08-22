// 🌈 Theme colors including resurrection
const themeColors = {
  grief: "#8B0000",
  renewal: "#228B22",
  contradiction: "#1E90FF",
  memory: "#DAA520",
  resurrection: "#FFD700", // gold
  default: "#999"
};

// 📦 Fragment data
const nodes = [
  { id: "f001", label: "Fragment 001", composted: false },
  { id: "f002", label: "Fragment 002", composted: false },
  { id: "f003", label: "Fragment 003", composted: false },
  { id: "f004", label: "Fragment 004", composted: true }
];

// 🔗 Link data with resurrection and drift
const links = [
  { source: "f001", target: "f002", drift_intensity: 1, theme: "grief" },
  { source: "f002", target: "f003", drift_intensity: 4, theme: "renewal" },
  { source: "f003", target: "f004", drift_intensity: 9, theme: "contradiction" },
  { source: "f001", target: "f004", drift_intensity: 2, theme: "memory", resurrected: true }
];

// 🧠 Filter toggle (set to true to show only compost/resurrection links)
const filterCompostOnly = false;

// 🧬 SVG setup
const svg = d3.select("svg");
const width = +svg.attr("width");
const height = +svg.attr("height");

// 🧲 Force simulation
const simulation = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).id(d => d.id).distance(100))
  .force("charge", d3.forceManyBody().strength(-300))
  .force("center", d3.forceCenter(width / 2, height / 2));

// 🔍 Filter links if needed
const visibleLinks = filterCompostOnly
  ? links.filter(d => d.resurrected || nodes.find(n => n.id === d.target).composted)
  : links;

// 🔗 Render links (fixed tooltip logic)
const linkGroup = svg.append("g")
  .attr("stroke-opacity", 0.6);

const link = linkGroup.selectAll("line")
  .data(visibleLinks)
  .join("line")
  .attr("stroke", d => d.resurrected ? themeColors.resurrection : (themeColors[d.theme] || themeColors.default))
  .attr("stroke-width", d => Math.sqrt(d.drift_intensity) * 2)
  .attr("stroke-dasharray", d => d.resurrected ? "4,2" : null);

link.append("title")
  .text(d => `Theme: ${d.theme}\nDrift Intensity: ${d.drift_intensity}${d.resurrected ? "\nResurrected from compost" : ""}`);

// 🟢 Render nodes
const nodeGroup = svg.append("g")
  .attr("stroke", "#fff")
  .attr("stroke-width", 1.5);

const node = nodeGroup.selectAll("circle")
  .data(nodes)
  .join("circle")
  .attr("r", 10)
  .attr("fill", d => d.composted ? "#555" : "#ccc")
  .call(drag(simulation));

node.append("title")
  .text(d => `${d.label}${d.composted ? " (Composted)" : ""}`);

// 🧲 Tick update
simulation.on("tick", () => {
  link.attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

  node.attr("cx", d => d.x)
      .attr("cy", d => d.y);
});

// 🖐️ Drag behavior
function drag(simulation) {
  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }

  return d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);
}
