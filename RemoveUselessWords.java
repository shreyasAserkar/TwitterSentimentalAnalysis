import java.io.IOException;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class RemoveUselessWords {

        public static void main(String[] args) throws Exception {

                Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "My new job");
        job.setJarByClass(RemoveUselessWords.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setReducerClass(SumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        job.waitForCompletion(true);
        System.exit(job.waitForCompletion(true) ? 0 : 1);
      }

        public static class TokenizerMapper extends Mapper< Object , Text, Text, IntWritable> {
                 IntWritable trackId = new IntWritable();
                 Text users = new Text();

            public void map(Object key, Text value, Context context)
                    throws IOException, InterruptedException {
                        String my = value.toString();
               String parts = my;
                if(my.contains("http"))
                {
                        parts = my.substring(0, my.indexOf("http"));        //splitting the data
                }



                    trackId.set(1);
                    users.set(parts.trim());
                    context.write(users, trackId);
           }
}

        public static class SumReducer extends
    Reducer< Text , IntWritable, Text, IntWritable> {
public void reduce(Text key, Iterable< IntWritable> values, Context context)
        throws IOException, InterruptedException {
    int sum = 0;
    for (IntWritable val : values) {
        sum += val.get(); 
    }
       context.write(new Text(key), new IntWritable(sum)); 
}
        }
}

