#!/usr/bin/node
const fileSystem = require('fs');
const t1 = process.argv[2];
const t2 = process.argv[3];
const t3 = process.argv[4];
let text = '';
text = text.concat(fileSystem.readFileSync(t1));
text = text.concat(fileSystem.readFileSync(t2));
fileSystem.writeFileSync(t3, text);
