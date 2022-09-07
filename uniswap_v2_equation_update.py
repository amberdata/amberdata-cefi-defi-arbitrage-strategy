


#swap_amount_eth_to_usdc( eth_amountIn = 2,  usdc_reserve = 102819284 , eth_reserve = 27978, fee_tier = 0.003)

def swap_amount_eth_to_usdc( eth_amountIn,  usdc_reserve , eth_reserve , fee_tier = 0.003,):

    eth_amountInWithFee = eth_amountIn * ( 1 - fee_tier)

    numerator = eth_amountInWithFee * usdc_reserve
    denominator = eth_reserve + eth_amountInWithFee

    usdc_amount_out = numerator * 1.00 / denominator

    return usdc_amount_out


def swap_amount_usdc_to_eth( usdc_amountIn, usdc_reserve , eth_reserve, fee_tier = 0.003):

    usdc_amountInWithFee = usdc_amountIn * ( 1 - fee_tier)

    numerator = usdc_amountInWithFee * eth_reserve
    denominator = usdc_reserve + usdc_amountInWithFee

    eth_amount_out = numerator * 1.00 / denominator

    return eth_amount_out