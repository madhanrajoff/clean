/*!

=========================================================
* Argon Design System React - v1.1.2
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-design-system-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-design-system-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classnames from "classnames";

// reactstrap components
import {
  Card,
  CardBody,
  NavItem,
  NavLink,
  Nav,
  TabContent,
  TabPane,
  Row,
  Col,
} from "reactstrap";

class TabsSection extends React.Component {
  state = {
    iconTabs: 1,
    plainTabs: 1,
  };
  toggleNavs = (e, state, index) => {
    e.preventDefault();
    this.setState({
      [state]: index,
    });
  };
  render() {
    return (
      <>
        <h3 className="h4 font-weight-bold mb-4 groom-heading-dark">Why Choose Us</h3>
        <Row className="justify-content-center">
          <Col lg="6">
            {/* Tabs with icons */}
            {/* <div className="mb-3">
              <small className="text-uppercase font-weight-bold">
                With icons
              </small>
            </div>
            <div className="nav-wrapper">
              <Nav
                className="nav-fill flex-column flex-md-row"
                id="tabs-icons-text"
                pills
                role="tablist"
              >
                <NavItem>
                  <NavLink
                    aria-selected={this.state.iconTabs === 1}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.iconTabs === 1,
                    })}
                    onClick={(e) => this.toggleNavs(e, "iconTabs", 1)}
                    href="#pablo"
                    role="tab"
                  >
                    <i className="ni ni-cloud-upload-96 mr-2" />
                    Home
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.iconTabs === 2}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.iconTabs === 2,
                    })}
                    onClick={(e) => this.toggleNavs(e, "iconTabs", 2)}
                    href="#pablo"
                    role="tab"
                  >
                    <i className="ni ni-bell-55 mr-2" />
                    Profile
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.iconTabs === 3}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.iconTabs === 3,
                    })}
                    onClick={(e) => this.toggleNavs(e, "iconTabs", 3)}
                    href="#pablo"
                    role="tab"
                  >
                    <i className="ni ni-calendar-grid-58 mr-2" />
                    Messages
                  </NavLink>
                </NavItem>
              </Nav>
            </div> */}
            <Card className="groom-shadow">
              <CardBody>
                <TabContent activeTab={"iconTabsStatic"}>
                  <TabPane tabId="iconTabsStatic">
                    <p className="groom-description">
                      <i className="fa fa-shield groom-icon" /> &nbsp; High-Quality Cleaning: Our professional team is dedicated to delivering a spotless, showroom-worthy shine for your vehicle.
                    </p>
                    <p className="groom-description">
                      <i className="fa fa-home groom-icon" /> &nbsp; At Your Doorstep: We come to you! Enjoy the luxury of a clean car without ever leaving your home or workplace.
                    </p>
                    <p className="groom-description">
                      <i className="fa fa-clock-o groom-icon" /> &nbsp; Your Time, Your Way: We work around your schedule. You choose the time slot that suits you, and we'll be there, without fail.                    
                    </p>
                    <p className="groom-description">
                      <i className="fa fa-car groom-icon" /> &nbsp; Experienced Professional Service: Our team of experienced car detailers is committed to providing you with the best possible car care experience. We take pride in ensuring your vehicle looks and feels its absolute best.
                    </p>
                  </TabPane>
                  <TabPane tabId="iconTabs2">
                    <p className="description">
                      Cosby sweater eu banh mi, qui irure terry richardson ex
                      squid. Aliquip placeat salvia cillum iphone. Seitan
                      aliquip quis cardigan american apparel, butcher voluptate
                      nisi qui.
                    </p>
                  </TabPane>
                  <TabPane tabId="iconTabs3">
                    <p className="description">
                      Raw denim you probably haven't heard of them jean shorts
                      Austin. Nesciunt tofu stumptown aliqua, retro synth master
                      cleanse. Mustache cliche tempor, williamsburg carles vegan
                      helvetica. Reprehenderit butcher retro keffiyeh
                      dreamcatcher synth.
                    </p>
                  </TabPane>
                </TabContent>
              </CardBody>
            </Card>
          </Col>
          <Col className="mt-5 mt-lg-0" lg="6">
            {/* Menu */}
            {/* <div className="mb-3">
              <small className="text-uppercase font-weight-bold">
                With text
              </small>
            </div>
            <div className="nav-wrapper">
              <Nav
                className="nav-fill flex-column flex-md-row"
                id="tabs-icons-text"
                pills
                role="tablist"
              >
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 1}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.plainTabs === 1,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 1)}
                    href="#pablo"
                    role="tab"
                  >
                    Home
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 2}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.plainTabs === 2,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 2)}
                    href="#pablo"
                    role="tab"
                  >
                    Profile
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 3}
                    className={classnames("mb-sm-3 mb-md-0", {
                      active: this.state.plainTabs === 3,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 3)}
                    href="#pablo"
                    role="tab"
                  >
                    Messages
                  </NavLink>
                </NavItem>
              </Nav>
            </div> */}
            <Card className="groom-shadow">
              <CardBody>
                <TabContent activeTab={"plainTabsStatic"}>
                  <TabPane tabId="plainTabsStatic">    
                    <p className="groom-description">
                      <i className="fa fa-calendar groom-icon" /> &nbsp; Auto-Renewal for Peace of Mind: We offer an auto-renewal option, so you can enjoy a continuous, hassle-free car cleaning experience. If you ever need to cancel, it's as simple as a click. We're here to make things easy for you.
                    </p>
                    <p className="groom-description">
                      <i className="fa fa-phone groom-icon" /> &nbsp; Dedicated Support at Your Fingertips: Have questions or need assistance? Our dedicated support team is just a call, WhatsApp message, or email away. We're here to ensure your experience is seamless.
                    </p>
                    <p className="groom-description">
                      <i className="fa fa-percent groom-icon" /> &nbsp; Exclusive Discounts for Active Customers: As a token of our appreciation, active customers enjoy discounted rates on any other car-related work they may need.                    
                    </p>
                  </TabPane>
                  <TabPane tabId="plainTabs2">
                    <p className="description">
                      Cosby sweater eu banh mi, qui irure terry richardson ex
                      squid. Aliquip placeat salvia cillum iphone. Seitan
                      aliquip quis cardigan american apparel, butcher voluptate
                      nisi qui.
                    </p>
                  </TabPane>
                  <TabPane tabId="plainTabs3">
                    <p className="description">
                      Raw denim you probably haven't heard of them jean shorts
                      Austin. Nesciunt tofu stumptown aliqua, retro synth master
                      cleanse. Mustache cliche tempor, williamsburg carles vegan
                      helvetica. Reprehenderit butcher retro keffiyeh
                      dreamcatcher synth.
                    </p>
                  </TabPane>
                </TabContent>
              </CardBody>
            </Card>
          </Col>
        </Row>

        <h3 className="h4 font-weight-bold mt-6 groom-heading-dark">Packages</h3>
        <Row className="justify-content-center groom-img">
        <Col className="mt-5 mt-lg-0" lg="10">
            {/* Menu */}
            <div className="nav-wrapper">
              <Nav
                className="nav-fill flex-column flex-md-row"
                id="tabs-icons-text"
                pills
                role="tablist"
              >
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 1}
                    className={classnames("mb-sm-3 mb-md-0 nav-link-groom", {
                      active: this.state.plainTabs === 1,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 1)}
                    href="#pablo"
                    role="tab"
                  >
                    Basic Clean
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 2}
                    className={classnames("mb-sm-3 mb-md-0 nav-link-groom", {
                      active: this.state.plainTabs === 2,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 2)}
                    href="#pablo"
                    role="tab"
                  >
                    Silver Shine
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 3}
                    className={classnames("mb-sm-3 mb-md-0 nav-link-groom", {
                      active: this.state.plainTabs === 3,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 3)}
                    href="#pablo"
                    role="tab"
                  >
                    Gold Standard
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    aria-selected={this.state.plainTabs === 4}
                    className={classnames("mb-sm-3 mb-md-0 nav-link-groom", {
                      active: this.state.plainTabs === 4,
                    })}
                    onClick={(e) => this.toggleNavs(e, "plainTabs", 4)}
                    href="#pablo"
                    role="tab"
                  >
                    Platinum Perfection
                  </NavLink>
                </NavItem>
              </Nav>
            </div>
            <Card className="groom-shadow">
              <CardBody>
                <TabContent activeTab={"plainTabs" + this.state.plainTabs}>
                  <TabPane tabId="plainTabs1">    
                    <p className="groom-description">
                      An excellent starter package for routine maintenance.
                    </p>
                    <img
                      alt="..."
                      className="img-fluid"
                      src={require("assets/img/theme/matthew-dockery-s99-JP8P3Hg-unsplash.jpg")}
                    />
                  </TabPane>
                  <TabPane tabId="plainTabs2">
                    <p className="groom-description">
                      A thorough cleaning with additional shine and gloss.
                    </p>
                    <img
                      alt="..."
                      className="img-fluid"
                      src={require("assets/img/theme/tim-schmidbauer-gJFaYN37KXM-unsplash.jpg")}
                    />
                  </TabPane>
                  <TabPane tabId="plainTabs3">
                    <p className="groom-description">
                      A premium package for a superior, all-round car makeover.
                    </p>
                    <img
                      alt="..."
                      className="img-fluid"
                      src={require("assets/img/theme/nick-kaufman-9U-Tgk61K7Y-unsplash.jpg")}
                    />
                  </TabPane>
                  <TabPane tabId="plainTabs4">
                    <p className="groom-description">
                      For those who demand nothing but the best. The epitome of car detailing.
                    </p>
                    <img
                      alt="..."
                      className="img-fluid"
                      src={require("assets/img/theme/reinhart-julian-_BK0NirjdG8-unsplash.jpg")}
                    />
                  </TabPane>
                </TabContent>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </>
    );
  }
}

export default TabsSection;
