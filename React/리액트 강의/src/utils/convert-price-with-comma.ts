export const convertPriceWithComma = (price: number) => {
  return price.toLocaleString()
}

export const currencyKR = (price: number) => `${convertPriceWithComma(price)}원`

// export default convertPriceWithComma

// export default {
//   convertPriceWithComma,
//   currencyKR
// }
