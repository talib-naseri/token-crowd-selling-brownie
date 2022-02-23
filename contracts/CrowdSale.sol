pragma solidity ^0.5.0;

import "@openzeppelin/contracts/crowdsale/Crowdsale.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CrowdSale is Crowdsale {
    constructor(
        uint256 rate,
        address payable wallet,
        address token
    ) public Crowdsale(rate, wallet, IERC20(token)) {}
}
