import React, { useState } from "react";
import styled from "styled-components";

import full from './images/star-rainbow.png';
import half from './images/star-half.png';
import none from './images/star-grey.png';

const SelectContainer = styled.div`
    width: 12.5rem;
`

const Container = styled.div`
    display: flex;
    align-items: center;

    .full {
        background-image: url(${full});
    }

    .half {
        background-image: url(${half});
    }

    .none {
        background-image: url(${none});
    }
`

const StarDiv = styled.div`
    background-size: cover;
    background-repeat: no-repeat;
    background-position: 50% 50%;
    width: 2.5em;
    height: 2.5em;
`

const StarInput = styled.input`
    appearance: none;
`

const colorCalc = (value, rating) => {
    const compare = rating - value;
    if (compare >= 0) return 'full';
    else if (compare === -0.5) return 'half';
    else return 'none';
}

const StarsDisplay = ({ defRating, rating, setRating, disabled, className }) => {

    const [hover, setHover] = useState(false);
    const [hoverRating, setHoverRating] = useState(0);

    const starHover = (e, value) => {
        e.stopPropagation();
        setHoverRating(value);
    }

    if (disabled) {
        return (
            <Container className={className}>
                <StarDiv className={colorCalc(1, defRating)}></StarDiv>
                <StarDiv className={colorCalc(2, defRating)}></StarDiv>
                <StarDiv className={colorCalc(3, defRating)}></StarDiv>
                <StarDiv className={colorCalc(4, defRating)}></StarDiv>
                <StarDiv className={colorCalc(5, defRating)}></StarDiv>
            </Container >
        )
    }

    return (
        <SelectContainer onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}>
            <Container className={className}>
                <StarDiv className={colorCalc(1, hover ? hoverRating : (rating ? rating : defRating))}
                    onMouseEnter={(e) => starHover(e, 1)}
                    onClick={(e) => setRating(1)}
                >
                    <StarInput type="radio" value="1" checked={1 === (rating ? rating : defRating)} onChange={(e) => setRating(1)} />
                </StarDiv>
                <StarDiv className={colorCalc(2, hover ? hoverRating : (rating ? rating : defRating))}
                    onMouseEnter={(e) => starHover(e, 2)}
                    onClick={(e) => setRating(2)}
                >
                    <StarInput type="radio" value="2" checked={2 === (rating ? rating : defRating)} onChange={(e) => setRating(2)} />
                </StarDiv>
                <StarDiv className={colorCalc(3, hover ? hoverRating : (rating ? rating : defRating))}
                    onMouseEnter={(e) => starHover(e, 3)}
                    onClick={(e) => setRating(3)}
                >
                    <StarInput type="radio" value="3" checked={3 === (rating ? rating : defRating)} onChange={(e) => setRating(3)} />
                </StarDiv>
                <StarDiv className={colorCalc(4, hover ? hoverRating : (rating ? rating : defRating))}
                    onMouseEnter={(e) => starHover(e, 4)}
                    onClick={(e) => setRating(4)}
                >
                    <StarInput type="radio" value="4" checked={4 === (rating ? rating : defRating)} onChange={(e) => setRating(4)} />
                </StarDiv>
                <StarDiv className={colorCalc(5, hover ? hoverRating : (rating ? rating : defRating))}
                    onMouseEnter={(e) => starHover(e, 5)}
                    onClick={(e) => setRating(5)}
                >
                    <StarInput type="radio" value="5" checked={5 === (rating ? rating : defRating)} onChange={(e) => setRating(5)} />
                </StarDiv>
            </Container >
        </SelectContainer>
    )
}

export default StarsDisplay
