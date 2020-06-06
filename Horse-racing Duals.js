const N = +(readline());
let indexes = []
for (let i = 0; i < N; i++) {
    indexes.push(+readline())
}
indexes = indexes.map(i => +i).sort((a, b) => a - b)
let min = Infinity
for (let i = 0; i < indexes.length - 1; i++) {
    let diff = indexes[i + 1] - indexes[i]
    if (diff < min) {
        min = diff
    }
}
console.log(min)
