import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Accordion from 'react-bootstrap/Accordion';
import { Row, Col} from 'react-bootstrap';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

var themeCodes = {
  gold: '#CDB450',
  green: '#001C12',
  white: '#E2E2E2'
}
var buttonStyles = {backgroundColor: themeCodes.green, color: themeCodes.white}

function ExampleCarouselImage(plan, width = 286, height = 180) {
  const carouselImages = {
    bronze: 'First slide',
    silver: 'Second slide',
    gold: 'Third slide',
  };
  
  let imageSrc = require(`./assets/${plan}.jpg`);
  let text = carouselImages[plan] || 'Default text'
  return (
    <Card.Img variant="top" src={imageSrc} alt={imageSrc} style={{ width: `${width}px`, height: `${height}px` }} />
  )
}

function App() {
  return (
    <Container>
      <Navbar className="mb-4" style={{backgroundColor: themeCodes.gold}}>
        <Container>
          <Navbar.Brand href="#home">Clean</Navbar.Brand>
          <Navbar.Toggle />
          <Navbar.Collapse className="justify-content-end">
            <Navbar.Text>
              Signed in as: <a href="#login">Mark Otto</a>
            </Navbar.Text>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Accordion  style={{backgroundColor: themeCodes.gold}}>
        <Accordion.Item eventKey="0">
          <Accordion.Header>Accordion Item #1</Accordion.Header>
          <Accordion.Body>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
            minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>Accordion Item #2</Accordion.Header>
          <Accordion.Body>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
            minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>

      <Row className="justify-content-md-center mt-4">
        <Col md="auto">
      <Card style={{ width: '18rem' }}>
      {ExampleCarouselImage('bronze')}
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <button type="button" class="btn btn-light" style={buttonStyles}>Go somewhere</button>
      </Card.Body>
    </Card>
    </Col>
    <Col md="auto">
      <Card style={{ width: '18rem' }}>
      {ExampleCarouselImage('silver')}
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <button type="button" class="btn btn-light" style={buttonStyles}>Go somewhere</button>
      </Card.Body>
    </Card>
    </Col>
    <Col md="auto">
      <Card style={{ width: '18rem' }}>
      {ExampleCarouselImage('gold')}
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <button type="button" class="btn btn-light" style={buttonStyles}>Go somewhere</button>
      </Card.Body>
    </Card>
    </Col>
    </Row>
    </Container>
  );
}

export default App;