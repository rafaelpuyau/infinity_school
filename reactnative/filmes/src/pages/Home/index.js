import React from 'react';
import { ScrollView } from 'react-native';

import { 
    Container, 
    SearchContainer, 
    Input, 
    SearchButton, 
    Title, 
    BannerButton,
    Banner,
    SliderMovie
} from './styles';

import { Feather } from '@expo/vector-icons';

import Header from '../../components/Header';
import SliderItem from '../../components/SliderItem';

function Home(){
    return(
        <Container>

            <Header title="React Prime"/>

            <SearchContainer>
                <Input 
                    placeholder = "Ex Star Wars"
                    placeholderTextColor = "#DDDDDD"
                />
                <SearchButton>
                    <Feather name="search" size={30} color="#FFFFFF" />
                </SearchButton>
            </SearchContainer>

            <ScrollView showsVerticalScrollIndicator={false}>

                <Title>Em cartaz</Title>

                <BannerButton activeOpacity={0.9} onPress={ () => alert('Cachorro')}>
                    <Banner 
                        resizeMethod="resize"
                        source={{uri: 'https://picsum.photos/id/237/200/300'}}
                    />
                </BannerButton>

                <SliderMovie
                    horizontal={true}
                    showsHorizontalScrollIndicator={false}
                    data={[1, 2, 3, 4]}
                    renderItem={ ({ item }) => <SliderItem /> }
                />

                <Title>Populares</Title>

                <SliderMovie
                    horizontal={true}
                    showsHorizontalScrollIndicator={false}
                    data={[1, 2, 3, 4]}
                    renderItem={ ({ item }) => <SliderItem /> }
                />

                <Title>Mais votados</Title>

                <SliderMovie
                    horizontal={true}
                    showsHorizontalScrollIndicator={false}
                    data={[1, 2, 3, 4]}
                    renderItem={ ({ item }) => <SliderItem /> }
                />

            </ScrollView>

        </Container>
    );
}

export default Home;