import { useEffect, useState } from "react";
import { Rings } from "react-loader-spinner";
import ReactTooltip from "react-tooltip";

type ResultProps = {
  running: boolean;
  data: Array<SearchResult>;
};

type SearchResult = {
  emoji: string;
  message: string;
  score: number;
};

const Result: React.FunctionComponent<ResultProps> = (props) => {
  if (props.data.length > 0) {
    return (
      <div className="result-list">
        {props.data.map((row, i) => {
          return (
            <div key={i} className="result-row">
              <Emoji emoji={row.emoji} />
              <div className="message">{row.message}</div>
            </div>
          );
        })}
      </div>
    );
  } else if (props.running) {
    return (
      <div className="loader">
        <Rings color="#aaa" height={60} width={60} />
      </div>
    );
  } else {
    return <div />;
  }
};

type EmojiProps = {
  emoji: string;
};

const Emoji: React.FunctionComponent<EmojiProps> = (props) => {
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    ReactTooltip.rebuild();
  }, [copied]);

  return (
    <div
      key={copied ? "copied" : "not-copied"}
      data-tip={copied ? "Copied!" : "Click to copy"}
      className="emoji"
      onClick={() => {
        navigator.clipboard.writeText(props.emoji);
        setCopied(true);
      }}
    >
      {props.emoji}
      <ReactTooltip
        className="tooltip"
        effect="solid"
        backgroundColor="#565869"
        arrowColor="transparent"
        offset={{ top: -6 }}
        delayShow={200}
        afterHide={() => setCopied(false)}
      />
    </div>
  );
};

export default Result;
