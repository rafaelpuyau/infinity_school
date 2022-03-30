import React from 'react';

import { 
    Container,
    BannerItem,
    Title,
    RateContainer,
    Rate
} from './styles';

import { Ionicons } from '@expo/vector-icons';

export default function SliderItem() {
    return(
        <Container activeOpacity={0.7}>
            <BannerItem
                source={{ uri: 'https://picsum.photos/id/237/200/300' }}
            />

            <Title numberOfLines={1}>Star Wars</Title>

            <RateContainer>
                <Ionicons name="md-star" size={12} color="#E7A74E" />
                <Rate>9/10</Rate>
            </RateContainer>
        </Container>
    )
}
