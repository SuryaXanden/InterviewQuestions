const N = parseInt(readline());
let indexes = []
for (let i = 0; i < N; i++) {
    indexes.push(+readline())
}
// indexes = indexes.sort()
let differences = {}
for( let i = 0 ; i < indexes.length ; i ++ ){
    for( let j = 0 ; j < indexes.length ; j ++ ){
        if( i != j ){
            let difference = Math.abs( indexes[i] - indexes[j] )
            if( difference ){
                const additional = [indexes[i] , indexes[j]].sort()
                if( difference in differences ){
                    differences[difference].concat( additional )
                }
                else{
                    differences[ difference ] = additional
                }
            }
        }
    }
}
const smallestDifference = Object.keys(differences).map(i=>+i)[0]
const valuesWithSmallestDifference = differences[ smallestDifference ]
// print( differences[ smallestDifference ].length )
print( smallestDifference )
