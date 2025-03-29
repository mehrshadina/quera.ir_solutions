#include <SFML/Graphics.hpp>
#include <vector>
#include <cmath>
#include <iostream>

const float initialHeight = 600.0f;
const float restitutionCoefficient = 0.8f;
const float gravity = 980.0f; 
const float epsilon = 0.5f;
const float radius = 20.0f; 
const float groundHeight = 50.0f;  

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 800), "Bouncing Ball Simulation");

    float height = initialHeight;
    float velocity = 0.0f;

    sf::CircleShape ball(radius);
    ball.setFillColor(sf::Color::Red);
    ball.setPosition(400.0f - radius, 800.0f - height - radius - groundHeight);

    sf::RectangleShape ground(sf::Vector2f(800.0f, groundHeight));
    ground.setFillColor(sf::Color(150, 75, 0));
    ground.setPosition(0, 800.0f - groundHeight);

    sf::Clock clock;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        float deltaTime = clock.restart().asSeconds();

        if (height > epsilon) {
            velocity += gravity * deltaTime;
            height -= velocity * deltaTime;

            if (height <= radius + groundHeight) {
                height = (radius + groundHeight) + restitutionCoefficient * (radius + groundHeight - height);
                velocity = -velocity * restitutionCoefficient;
            }

            ball.setPosition(400.0f - radius, 800.0f - height - groundHeight - radius);
        }

        window.clear(sf::Color::White);
        window.draw(ball);
        window.draw(ground);
        window.display();
    }

    return 0;
}
