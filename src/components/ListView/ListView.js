import React, { useState } from "react";
import {
  Divider,
  Collapse,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Button,
} from "@material-ui/core";
import { ExpandLess, ExpandMore, ArrowForwardIos } from "@material-ui/icons";
import uniqid from "uniqid";

const ListView = ({ meaning, t }) => {
  const [open, setOpen] = useState(false);
  const [length, SetLength] = useState(10);
  const handleClick = () => {
    setOpen(!open);
  };
  const showMore = () => {
    var currentLenght = length;
    currentLenght += 5;
    SetLength(currentLenght);
  };

  return (
    <div>
      <ListItem button key={uniqid()} onClick={handleClick}>
        <ListItemText primary={t("Meaning") + meaning.id + ":"} />
        {open ? <ExpandLess /> : <ExpandMore />}
      </ListItem>
      <Collapse key={uniqid()} in={open} timeout="auto" unmountOnExit>
        <List component="li" disablePadding key={uniqid()}>
          {meaning.examples.slice(0, length).map((example) => {
            return (
              <ListItem button key={uniqid()}>
                <ListItemIcon>
                  <ArrowForwardIos />
                </ListItemIcon>
                <ListItemText key={uniqid()} primary={t(example.example)} />
              </ListItem>
            );
          })}
          {length !== meaning.examples.length &&
          meaning.examples.length > length ? (
            <Button
              style={{ width: "100%", height: "60%", minWidth: "20%" }}
              key={uniqid()}
              onClick={showMore}
            >
              {t("Show More")}
            </Button>
          ) : null}
        </List>
      </Collapse>
      <Divider />
    </div>
  );
};
export default ListView;
