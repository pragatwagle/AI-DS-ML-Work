
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Reducer.Context;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class CCFinalRound extends Configured implements Tool {

	public static class CCFinalRoundMapper extends Mapper<Text, Text, Text, Text> {

		private Configuration conf;

		@Override
		public void setup(Context context) throws IOException, InterruptedException {
			conf = context.getConfiguration();
		}

		public void map(Text nodeId, Text value, Context context) throws IOException, InterruptedException {
			// Example of line: 
			// 6	0:5,7,8 ~~ NodeId	CompId:AjList

			// get the curr node id to string
			String currNodeId = nodeId.toString();

			// get the compID separated by colon to the adjacent list
			String compIDAjList = value.toString();

			// split the compIDAjlist into an array of compID and ajacent nodes 
			ArrayList<String> splitCompIdAdjList = new ArrayList<String>(Arrays.asList(compIDAjList.split(":")));
			if (splitCompIdAdjList.size() >= 2) {

			// assign the compid to compID
			String compID = splitCompIdAdjList.get(0);
			// split the string of ajacent nodes into an array list by a comma
			String  ajListStr = splitCompIdAdjList.get(1);

			// Split string at comma and comvert into arraylist of type string
			ArrayList<String> ajList = new ArrayList<String>(Arrays.asList(ajListStr.split(",")));

			//write out the compID and the curNodeID
			context.write(new Text(compID),new Text(currNodeId));

			for(String aj: ajList)
			{
				//iterate and write out each compid and each adjacent node ID
				System.out.println(compID + "	" + aj );
				context.write(new Text(compID), new Text(aj));
			}
		    }
			// Output Style : 
			//			CompID	NodeID
			//				1	1
			//				1	2
		}	//				1	3
	}

	public static class CCFinalRoundReducer extends Reducer<Text, Text, Text, Text> {
		
		private Configuration conf;
		@Override
		public void setup(Context context) throws IOException, InterruptedException {
			conf = context.getConfiguration();
		}

		public void reduce(Text compId, Iterable<Text> nodeValues, Context context) throws IOException, InterruptedException {
			// input of each line is the compID. a tab, and then NodeID
			HashSet<String> arrayValues = new HashSet<String>();
			for (Text value : nodeValues) {
				arrayValues.add(value.toString());
			}
			String listString = String.join(", ", arrayValues);
			context.write(new Text(compId), new Text(listString));
		}
	}

	@Override
	public int run(String[] args) throws Exception {

		Path in = new Path(args[0]);
		Path out = new Path(args[1]);


		Configuration conf;
		Job job;

		conf = getConf();
	

		boolean runExitCode = false;
		job = Job.getInstance(conf, "CCFinalRound");

		job.setJarByClass(CCFinalRound.class);

		FileInputFormat.setInputPaths(job, in);
		FileOutputFormat.setOutputPath(job, out);

		job.setMapperClass(CCFinalRoundMapper.class);
		job.setReducerClass(CCFinalRoundReducer.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		job.setInputFormatClass(KeyValueTextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		runExitCode = job.waitForCompletion(true);
		return runExitCode ? 0 : 1;
	}

	public static void main(String[] args) throws Exception {
		int runExitCode = ToolRunner.run(new CCFinalRound(), args);
		System.exit(runExitCode);
	}
}

