const svg = d3.select("svg");

// 🎨 Color mapping by fragment type
const colorMap = {
  preserved: "#4CAF50",
  composted: "#F44336",
  anomaly: "#FF9800"
};

// 🧩 Generate links based on fragment order
function generateLinks(nodes) {
  const links = [];
  for (let i = 0; i < nodes.length - 1; i++) {
    links.push({ source: nodes[i].id, target: nodes[i + 1].id });
  }
  return links;
}

// 🧠 Reinterpretation engine
function simulatePair(fragment) {
  return {
    ...fragment,
    text: `[Reinterpreted] ${fragment.text}`,
    timestamp: new Date().toISOString()
  };
}

// ⚖️ Contradiction detector
function detectContradiction(original, reinterpretation) {
  return original.text === reinterpretation.text ? 0 : 0.8;
}

// 🧪 Composting logic
function compostFragment(original, reinterpretation, contradiction) {
  let outcome;
  if (contradiction < 0.2) {
    outcome = "preserved";
  } else if (contradiction > 0.7) {
    outcome = "composted";
  } else {
    outcome = "anomaly";
  }

  original.type = outcome;
  console.log(`🧪 Composting outcome for ${original.id}: ${outcome}`);
}

// 🌌 Drift trail animation
function renderDriftTrail(original, reinterpretation) {
  svg.append("line")
    .attr("x1", original.x)
    .attr("y1", original.y)
    .attr("x2", original.x + Math.random() * 40 - 20)
    .attr("y2", original.y + Math.random() * 40 - 20)
    .attr("stroke", "#FFD700")
    .attr("stroke-width", 2)
    .attr("stroke-dasharray", "4 2")
    .transition()
    .duration(3000)
    .style("opacity", 0)
    .remove();
}

// 🌙 Recursive Dimulste loop
function feedToDimulste(fragment, depth = 0, maxDepth = 3) {
  if (depth >= maxDepth) {
    console.log(`🌙 Dimulste loop complete for ${fragment.id}`);
    return;
  }

  const reinterpretation = simulatePair(fragment);
  const contradiction = detectContradiction(fragment, reinterpretation);
  compostFragment(fragment, reinterpretation, contradiction);

  logEvent({
    type: "dimulste-rehearsal",
    fragmentId: fragment.id,
    depth,
    original: fragment,
    reinterpretation,
    contradiction
  });

  console.log(`🔁 Dimulste depth ${depth} → ${fragment.id} → ${reinterpretation.text}`);

  // Recursive call
  feedToDimulste(reinterpretation, depth + 1, maxDepth);
}

// 📜 Event logger
function logEvent(eventObj) {
  console.log("🧠 Rehearsal Event:", eventObj);
}

// 🧠 Main render function
function renderGraph(nodes, links) {
  const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(120))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(window.innerWidth / 2, window.innerHeight / 2))
    .alphaDecay(0.01)
    .alpha(1)
    .restart();

  const tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("position", "absolute")
    .style("padding", "8px")
    .style("background", "#222")
    .style("color", "#eee")
    .style("border-radius", "4px")
    .style("font-size", "14px")
    .style("pointer-events", "none")
    .style("opacity", 0);

  const link = svg.selectAll(".link")
    .data(links)
    .enter().append("line")
    .attr("stroke", "gray")
    .attr("stroke-width", 2);

  const node = svg.selectAll(".node")
    .data(nodes)
    .enter().append("circle")
    .attr("r", 20)
    .attr("fill", d => colorMap[d.type] || "gray")
    .attr("stroke", "black")
    .attr("stroke-width", 2)
    .on("mouseover", (event, d) => {
      tooltip.transition().duration(200).style("opacity", 0.9);
      tooltip.html(d.text || "No fragment text")
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY - 28) + "px");
    })
    .on("mouseout", () => {
      tooltip.transition().duration(300).style("opacity", 0);
    })
    .on("click", function(event, d) {
      const timestamp = new Date().toISOString();

      const reinterpretation = simulatePair(d);
      const contradiction = detectContradiction(d, reinterpretation);

      logEvent({
        type: "click-rehearsal",
        fragmentId: d.id,
        timestamp,
        original: d,
        reinterpretation,
        contradiction
      });

      d3.select(this)
        .transition()
        .duration(300)
        .attr("r", contradiction > 0.5 ? 28 : 20)
        .style("fill", contradiction > 0.5 ? "#ff6666" : "#66ccff");

      d.reinterpretation = reinterpretation;
      compostFragment(d, reinterpretation, contradiction);
      renderDriftTrail(d, reinterpretation);
      feedToDimulste(reinterpretation); // Recursive loop starts here
    });

  const labels = svg.selectAll(".label")
    .data(nodes)
    .enter().append("text")
    .text(d => d.label)
    .attr("font-size", "12px")
    .attr("text-anchor", "middle")
    .attr("fill", "#ccc");

  simulation.on("tick", () => {
    link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

    node
      .attr("cx", d => d.x)
      .attr("cy", d => d.y);

    labels
      .attr("x", d => d.x)
      .attr("y", d => d.y - 25);
  });
}

// 📦 Load fragments from JSON
d3.json("fragments.json").then(data => {
  const nodes = data;
  const links = generateLinks(nodes);
  renderGraph(nodes, links);
});
