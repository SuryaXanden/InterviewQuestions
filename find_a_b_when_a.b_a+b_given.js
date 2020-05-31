// Program to find A & B when A+B and A*B is given

const S = 1652
const P = 676500

for (let A = 2; A < P / 2; A++) {
    const B = P / A
    if (B == ~~B && A + B == S) {
        console.log(A, B)
        break
    }
}
