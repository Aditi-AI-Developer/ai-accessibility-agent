const fs = require("fs");
const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;

function parseJSX(code) {
  const ast = parser.parse(code, {
    sourceType: "module",
    plugins: ["jsx", "typescript"],
  });

  let elements = [];

  traverse(ast, {
    JSXOpeningElement(path) {
      const node = path.node;

      let name = "";
      if (node.name.type === "JSXIdentifier") {
        name = node.name.name;
      } else if (node.name.type === "JSXMemberExpression") {
        name = node.name.property.name;
      }

      const attributes = node.attributes
        .map((attr) => {
          if (attr.type === "JSXAttribute" && attr.name) {
            return attr.name.name;
          }
          return null;
        })
        .filter(Boolean);

      const line = node.loc ? node.loc.start.line : null;

      elements.push({
        name,
        attributes,
        line,
      });
    },
  });

  return elements;
}

function main() {
  const filePath = process.argv[2];

  if (!filePath) {
    console.error("No file path provided");
    process.exit(1);
  }

  try {
    const code = fs.readFileSync(filePath, "utf-8");
    const result = parseJSX(code);
    console.log(JSON.stringify(result));
  } catch (error) {
    console.error("Error:", error.message);
    process.exit(1);
  }
}

main();